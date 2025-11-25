from cassandra.cluster import Cluster
from cassandra.policies import RoundRobinPolicy
from .config import settings

cluster: Cluster | None = None
session = None

def get_cluster() -> Cluster:
    global cluster
    if cluster is None:
        contact_points = []
        ports = []

        # separar host y puerto de cada contact point (host:port)
        for cp in settings.CASSANDRA_CONTACT_POINTS:
            cp = cp.strip()
            if ":" in cp:
                host, port_str = cp.split(":")
                contact_points.append(host)
                ports.append(int(port_str))
            else:
                contact_points.append(cp)

        # si no se definieron puertos explícitos, Cassandra usa 9042
        # pero el driver solo permite un solo puerto, así que
        # manejamos el primer puerto o el default
        port = ports[0] if ports else 9042

        cluster = Cluster(
            contact_points=contact_points,
            port=port,
            load_balancing_policy=RoundRobinPolicy()
        )
    return cluster

def get_session():
    global session
    if session is None:
        cluster = get_cluster()
        session = cluster.connect(settings.CASSANDRA_KEYSPACE)
        print("[CASSANDRA] Conectado al keyspace:", settings.CASSANDRA_KEYSPACE)
    return session

def shutdown():
    global cluster, session
    if session:
        session.shutdown()
    if cluster:
        cluster.shutdown()
    session = None
    cluster = None

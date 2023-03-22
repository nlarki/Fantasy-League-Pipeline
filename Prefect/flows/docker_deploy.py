from prefect.infrastructure.docker import DockerContainer
from prefect.deployments import Deployment
from etl_gcs_player import etl_parent_flow

docker_block = DockerContainer.load("fpl")

docker_dep = Deployment.build_from_flow(
    flow=etl_parent_flow,
    name='docker_player_flow',
    infrastructure=docker_block
)

if __name__ == "__main__":
    docker_dep.apply()

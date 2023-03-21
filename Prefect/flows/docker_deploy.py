from prefect.infrastructure.docker import DockerContainer
from prefect.deployments import Deployment
from etl_gcs_player import etl_parent_flow
from etl_gcs_teams import etl_parent_flows

docker_block = DockerContainer.load("fpl")

docker_dep = Deployment.build_from_flow(
    flow=etl_parent_flow,
    name='docker_player_flow',
    infrastructure=docker_block
)

docker_dep_team = Deployment.build_from_flow(
    flow=etl_parent_flows,
    name='docker_teams_flow',
    infrastructure=docker_block
)

if __name__ == "__main__":
    docker_dep.apply()
    docker_dep_team.apply()
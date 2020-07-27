# Watchtower GitLab Deploy

This project packs a GitLabCI compatible image to trigger updates in any public Watchtower instance running in HTTP API mode.

## Usage

In your `.gitlab-ci.yml`, create a job in which the update action will occur and set `victorcmoura/watchtower-gitlab-deploy` as its base image:

```yml
trigger_watchtower_update:
  stage: deploy
  image: victorcmoura/watchtower-gitlab-deploy
  script:
    - update
  only:
    - master
```

To work properly, the following environment variables have to be set in GitLabCI's configs:

| Varible | Description | Type | Example |
|---------|-------------|------|---------|
| WATCHTOWER_API_TOKEN | Watchtower HTTP API authorization token. | string | mytoken123 |
| WATCHTOWER_API_HOSTNAME | Watchtower HTTP API host address. | string | http://example.com |

Before running in GitLabCI, you might want to test your instance's public connectivity by running:

```sh
docker run -e WATCHTOWER_API_TOKEN=<your token> -e WATCHTOWER_API_HOSTNAME=<your hostname> victorcmoura/watchtower-gitlab-deploy update
```
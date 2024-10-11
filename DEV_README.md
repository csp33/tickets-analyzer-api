# Pushing the image

```shell
export IMAGE_TAG=1.2.0
docker buildx build --push --platform linux/arm64,linux/amd64 -t csp33/tickets-analyzer-api:$IMAGE_TAG -t csp33/tickets-analyzer-api:latest .
```

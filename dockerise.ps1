param(
    [string]$Tag
)

Write-Host "Building Docker image with tag: $Tag"
docker build -t myapp:$Tag .

Write-Host "Docker image built successfully."

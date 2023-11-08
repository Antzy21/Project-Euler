# Project-Euler

Python solutions I wrote back in 2017 when first learning to program!
https://projecteuler.net/

## Docker setup
To build the image

`docker image build -t prjeulapi .`

To run the container

`docker run -d -p 5432:5000 --name prjeul prjeulapi`
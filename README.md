# qrcode-generator
- This helps in the build of qrcode generated via PYTHON and activated via DOCKER.
- This QRCode generated will work same for mostly every dependencies as it requires the basic dependencies which are required to run a system.

  ## Getting Started
  1. Clone or download this repository to your local machine.
  2. To run this you nedd to have DOCKER DESKTOP and PYTHON installed on your system.
  3. For python packages refer to the [requirements.txt](requirements.txt)
     ```bash
     pip install fastapi
     pip install pydantic
     pip install uvicorn
     pip install qrcode
  4. To run this in Docker first run the following commands (to build and run) in your terminal where the project is cloned.
     ```bash
     docker docker build -t qr-code-generator-app.
     docker run -d -p 80:80 qr-code-generator-app
  5. Now, open the Docker Desktop and see whether if the Container is created or not, if not try again.
  6. If yes, the go to your default browser and type
     ```bash
     localhost
    in the address bar. The output retured should be
     ```bash
     {"Hello":"World"}
7. Now, type the following in the address bar to generate a qrcode of 'abc'
     ```bash
     http://localhost/qrcode/?query=abc
  8. To change it to other word or direct to a website (e.g. "www.google.com"), replace the word 'abc' with it.
     ```bash
     http://localhost/qrcode/?query=www.google.com
   

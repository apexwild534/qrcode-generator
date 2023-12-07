from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import qrcode
from io import BytesIO

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/qrcode/")
async def create_qrcode(query: str):
    qr = qrcode.QRCode()
    qr.add_data(query)

    img = qr.make_image(fill="black", back_color="white")
    img_io = BytesIO()
    img.save(img_io, "PNG")
    img_io.seek(0)

    return StreamingResponse(img_io, media_type="image/png")

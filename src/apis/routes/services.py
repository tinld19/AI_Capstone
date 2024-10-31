# import os

# from typing import List

# from fastapi import APIRouter, File, UploadFile, Request, HTTPException
# from fastapi.responses import JSONResponse
# from starlette import status

# router = APIRouter()


# @router.post("/gen-answer", status_code=status.HTTP_200_OK)
# async def gen_answer_chat(request: Request):
#    try:
#       body = await request.json()
#       question = body["question"]
#       chatBot = ChatBot()
#       response, rl = chatBot.gen_answer(question)
#       return {"answer": response, "domain": rl}
#    except Exception as e:
#       raise HTTPException(status_code=500, detail=f"Error generating answer: {str(e)}")


# @router.post("/classify/upload", tags=["file_upload"], status_code=status.HTTP_200_OK)
# async def file_inference(files: List[UploadFile] = File(...)):
#     upload_folder = "./uploaded_files"
#     os.makedirs(upload_folder, exist_ok=True)
#     paths = []
#     for file in files:
#         file_path = os.path.join(upload_folder, file.filename)
#         with open(file_path, "wb") as f:
#             f.write(await file.read())
#         paths.append(file_path)
#     return JSONResponse(status_code=status.HTTP_200_OK, content={"results": paths})
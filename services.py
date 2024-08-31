# from dataclasses import dataclass, field
# from fastapi import FastAPI, Request, Response, File, UploadFile
# from typing import List
# from src.akaBot.search import ChatBot
# # import os
# import orjson

# @dataclass
# class Services:
#    """API Services"""
#    app: "FastAPI" = field(default_factory=FastAPI)
#    request: Request = field(default=None)
#    response: Response = field(default=None)

#    # define router here
#    def __post_init__(self):
#       """Post init"""
#       self.app.post("gen-answer")(self.gen_answer)

#    async def gen_answer(self, request: Request):
#       body = await request.json()
#       data = orjson.loads(body)
#       question = data.get("question")
#       chatBot = ChatBot()
#       response = chatBot.gen_answer(question)
#       return {"Answer": response}

#    @property
#    def __call__(self):
#       return self.app
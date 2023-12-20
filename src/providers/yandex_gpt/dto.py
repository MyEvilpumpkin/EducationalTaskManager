"""
Module that contains data transfer objects classes definitions

All classes are required to work with the YandexGPT API
Accordingly, see the documentation for these classes in the API documentation
"""

import pydantic  # Required to define classes


class Message(pydantic.BaseModel):
    role: str
    text: str

    @staticmethod
    def system_message(text: str):
        return Message(
            role='system',
            text=text
        )

    @staticmethod
    def user_message(text: str):
        return Message(
            role='user',
            text=text
        )

    @staticmethod
    def assistant_message(text: str):
        return Message(
            role='assistant',
            text=text
        )


class Options(pydantic.BaseModel):
    stream: bool
    temperature: float
    maxTokens: int

    @staticmethod
    def default():
        return Options(
            stream=False,
            temperature=1,
            maxTokens=1000
        )


class Request(pydantic.BaseModel):
    modelUri: str
    completionOptions: Options
    messages: list[Message]


class Alternative(pydantic.BaseModel):
    message: Message
    status: str


class Usage(pydantic.BaseModel):
    completionTokens: str
    inputTextTokens: str
    totalTokens: str


class Result(pydantic.BaseModel):
    alternatives: list[Alternative]
    modelVersion: str
    usage: Usage


class Response(pydantic.BaseModel):
    result: Result


class OAuthToken(pydantic.BaseModel):
    yandexPassportOauthToken: str

    @staticmethod
    def token(oauth_token: str):
        return OAuthToken(
            yandexPassportOauthToken=oauth_token
        )


class IAMToken(pydantic.BaseModel):
    iamToken: str
    expiresAt: str

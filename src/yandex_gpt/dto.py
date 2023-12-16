import pydantic


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


class CompletionOptions(pydantic.BaseModel):
    stream: bool
    temperature: float
    maxTokens: int


class Request(pydantic.BaseModel):
    modelUri: str
    completionOptions: CompletionOptions
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


class IAMToken(pydantic.BaseModel):
    iamToken: str
    expiresAt: str

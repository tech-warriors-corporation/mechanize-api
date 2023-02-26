from projects.commons.enums.status_code_enum import StatusCodeEnum

class ResponseHelper:
    @staticmethod
    def generate(payload = None, status_code: StatusCodeEnum = StatusCodeEnum.OK.value):
        return { 'payload': payload }, status_code

import sys


def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    
    file_name = exc_tb.tb_frame.f_code.co_filename  

    error_message = f"Error occured in python script name {0}, line number {1} and error message is {2}".format(file_name,exc_tb.tb_lineno,str(error))


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message_detail(error_message,error_detail))













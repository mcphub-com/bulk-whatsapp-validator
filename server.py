import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/inutil-inutil-default/api/bulk-whatsapp-validator'

mcp = FastMCP('bulk-whatsapp-validator')

@mcp.tool()
def validate_up_to1000(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Enter an array of up to 1000 numbers to validate.'''
    url = 'https://bulk-whatsapp-validator.p.rapidapi.com/eb1000'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'bulk-whatsapp-validator.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def validate_up_to100(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Enter an array of up to 100 numbers to validate.'''
    url = 'https://bulk-whatsapp-validator.p.rapidapi.com/eb100'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'bulk-whatsapp-validator.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def validate_up_to10(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Enter an array of up to 10 numbers to validate.'''
    url = 'https://bulk-whatsapp-validator.p.rapidapi.com/eb10'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'bulk-whatsapp-validator.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def validate_single_whatsapp_number(phone: Annotated[Union[int, float], Field(description='The whatsapp number must be written as: number (including countrycode); do NOT include any non-number character, spaces, or anything which is not a number. Examples: of correct numbers are: 34123456789 (for spain) or 491234567890 (for Germany). Default: 34605797764')]) -> dict: 
    '''Enter a single phone number you want to validate.'''
    url = 'https://bulk-whatsapp-validator.p.rapidapi.com/wchk'
    headers = {'x-rapidapi-host': 'bulk-whatsapp-validator.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'phone': phone,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def is_abusiness(phone: Annotated[Union[int, float], Field(description='The whatsapp number must be written as: countrycode and number; do NOT include any non-number character, spaces, or anything which is not a number. Examples: of correct numbers are: 34123456789 (for spain) or 491234567890 (for Germany). Default: 34655719560')]) -> dict: 
    '''Requests to this endpoint will return `true` if the number is a Whatsapp for Business account, or `false` if it's not.'''
    url = 'https://bulk-whatsapp-validator.p.rapidapi.com/isbiz'
    headers = {'x-rapidapi-host': 'bulk-whatsapp-validator.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'phone': phone,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def about_info(phone: Annotated[Union[int, float], Field(description='Default: 34605797764')]) -> dict: 
    '''This endpoint will return the *About* state of the WA number on the query.'''
    url = 'https://bulk-whatsapp-validator.p.rapidapi.com/about'
    headers = {'x-rapidapi-host': 'bulk-whatsapp-validator.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'phone': phone,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")

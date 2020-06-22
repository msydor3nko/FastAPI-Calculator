from fastapi import FastAPI, Depends
from models import CalcGetRequest, CalcResponce

# init FastAPI app
app = FastAPI()


# showing math operation and a result
@app.get('/calc', summary='Calc as get method', response_model=CalcResponce)
async def get_calc(query: CalcGetRequest = Depends(CalcGetRequest)):
    params = query.dict()
    responce = {'result': '', 'operation': '', 'uid': ''}
    responce['result'] = eval(params['expression'])
    responce['operation'] = params['expression']
    return responce
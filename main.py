from japronto import Application

def hello(request):
    return request.Response(text='Hello world')

def calc(request):
    return request.Response(
        json = {
            "hello": f"{request.match_dict['data']}"
        },
        code = 200
    )

app = Application()

app.router.add_route('/', hello)
app.router.add_route('/calc/{data}', calc, methods=['GET'])

app.run(debug=True)

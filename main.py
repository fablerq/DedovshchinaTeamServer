from japronto import Application

def hello(request):
    return request.Response(text='Hello world')

def calc(request):
    return request.Response(
        json = {
            "id": 1,
            "initial": "str",
            "level": "str",
            "country": "str",
            "region": "str",
            "city": "city",
            "place": "place",
            "area_type": "str",
            "area": "str",
            "street_type": "str",
            "house": "str",
            "building": "str",
            "flat": "str",
            "office": "str"
        },
        code = 200
    )

app = Application()

app.router.add_route('/', hello)
app.router.add_route('/calc/{data}', calc, methods=['GET'])

print("starting")
app.run()
print("end")

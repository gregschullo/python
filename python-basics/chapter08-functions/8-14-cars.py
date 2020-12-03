def build_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    
    return car_info

new_car = build_car('toyota', 'tacoma', color='tan', year=2017)
print(new_car)

car = build_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

new_car = build_car('toyota', 'corolla', color='silver', year=2010)
print(new_car)

from swagger_tester import swagger_test

authorize_error = {
   'post': {
       '/pet/{petId}': [200],
       '/pet': [200]
   },
   'put': {
       '/user/{username}': [200],
       '/pet': [200]
   },
   'delete': {
       '/pet/{petId}': [200],
       '/store/order/{orderId}': [200],
       '/user/{username}': [200]
   }
}

if __name__ == '__main__':
	# swagger_test('petstore_swagger.json', authorize_error=authorize_error, wait_between_test=True)
	swagger_test(app_url='http://petstore.swagger.io/v2', authorize_error=authorize_error)
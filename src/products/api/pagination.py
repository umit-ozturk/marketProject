from rest_framework import pagination



class StandartResultsPagination(pagination.PageNumberPagination):
	page_size = 4
	page_size_query_param = 'page_size'
	max_page_size = 1000

class FeaturedResultsPagination(pagination.PageNumberPagination):
	page_size = 3
	page_size_query_param = 'page_size'
	max_page_size = 1000

class StandartMainPageProductResultsPagination(pagination.PageNumberPagination):
	page_size = 20
	page_size_query_param = 'page_size'
	max_page_size = 1000	
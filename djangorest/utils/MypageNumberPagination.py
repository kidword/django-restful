from rest_framework.pagination import PageNumberPagination


class PageNumber(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'  # 每页显示
    max_page_size = 5  # 最大页码

    page_query_param = 'page'

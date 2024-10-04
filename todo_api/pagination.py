from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size_query_param = 'limit'  # Use 'limit' for controlling page size
    # page_size = 10  # Default page size (optional, can be overridden in settings)

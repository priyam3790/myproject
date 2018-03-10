from rest_framework.pagination import *


class PageLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10


class PagePagination(PageNumberPagination):
    page_size = 2

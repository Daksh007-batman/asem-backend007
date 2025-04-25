from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    # Let DRF handle known exceptions (ValidationError, NotFound, etc.)
    response = exception_handler(exc, context)

    if response is not None:
        return response

    # For unhandled exceptions, log and return a generic error
    logger.error(f"Unhandled exception: {str(exc)} in {context['view']}")
    return Response(
        {"detail": "Internal server error. Please contact support."},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )

# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.6.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from intrinio_sdk.api_client import ApiClient


class FundamentalsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_fundamental_by_id(self, id, **kwargs):  # noqa: E501
        """Fundamental by ID  # noqa: E501

        Returns detailed fundamental data for the given `id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fundamental_by_id(id, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The Intrinio ID for the Fundamental (required)
        :return: Fundamental
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_fundamental_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_fundamental_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_fundamental_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Fundamental by ID  # noqa: E501

        Returns detailed fundamental data for the given `id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fundamental_by_id_with_http_info(id, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The Intrinio ID for the Fundamental (required)
        :return: Fundamental
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fundamental_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_fundamental_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/fundamentals/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Fundamental',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_fundamental_reported_financials(self, id, **kwargs):  # noqa: E501
        """Reported Financials  # noqa: E501

        Returns the As-Reported Financials directly from the financial statements of the XBRL filings from the company  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fundamental_reported_financials(id, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The Intrinio ID or lookup code (ticker-statement-year-period) for the Fundamental (required)
        :return: ApiResponseReportedFinancials
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_fundamental_reported_financials_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_fundamental_reported_financials_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_fundamental_reported_financials_with_http_info(self, id, **kwargs):  # noqa: E501
        """Reported Financials  # noqa: E501

        Returns the As-Reported Financials directly from the financial statements of the XBRL filings from the company  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fundamental_reported_financials_with_http_info(id, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The Intrinio ID or lookup code (ticker-statement-year-period) for the Fundamental (required)
        :return: ApiResponseReportedFinancials
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fundamental_reported_financials" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_fundamental_reported_financials`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/fundamentals/{id}/reported_financials', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseReportedFinancials',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_fundamental_standardized_financials(self, id, **kwargs):  # noqa: E501
        """Standardized Financials  # noqa: E501

        Returns professional-grade historical financial data. This data is standardized, cleansed and verified to ensure the highest quality data sourced directly from the XBRL financial statements. The primary purpose of standardized financials are to facilitate comparability across a single company’s fundamentals and across all companies fundamentals. For example, it is possible to compare total revenues between two companies as of a certain point in time, or within a single company across multiple time periods. This is not possible using the as reported financial statements because of the inherent complexity of reporting standards.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fundamental_standardized_financials(id, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The Intrinio ID or lookup code (ticker-statement-year-period) for the Fundamental (required)
        :return: ApiResponseStandardizedFinancials
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_fundamental_standardized_financials_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_fundamental_standardized_financials_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_fundamental_standardized_financials_with_http_info(self, id, **kwargs):  # noqa: E501
        """Standardized Financials  # noqa: E501

        Returns professional-grade historical financial data. This data is standardized, cleansed and verified to ensure the highest quality data sourced directly from the XBRL financial statements. The primary purpose of standardized financials are to facilitate comparability across a single company’s fundamentals and across all companies fundamentals. For example, it is possible to compare total revenues between two companies as of a certain point in time, or within a single company across multiple time periods. This is not possible using the as reported financial statements because of the inherent complexity of reporting standards.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fundamental_standardized_financials_with_http_info(id, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The Intrinio ID or lookup code (ticker-statement-year-period) for the Fundamental (required)
        :return: ApiResponseStandardizedFinancials
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fundamental_standardized_financials" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_fundamental_standardized_financials`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/fundamentals/{id}/standardized_financials', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseStandardizedFinancials',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def lookup_fundamental(self, identifier, statement_code, fiscal_year, fiscal_period, **kwargs):  # noqa: E501
        """Lookup Fundamental  # noqa: E501

        Returns the Fundamental for the Company with the given `identifier` and with the given parameters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.lookup_fundamental(identifier, statement_code, fiscal_year, fiscal_period, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: A Company identifier (Ticker, CIK, LEI, Intrinio ID) (required)
        :param str statement_code: The statement code (required)
        :param int fiscal_year: The fiscal year (required)
        :param str fiscal_period: The fiscal period (required)
        :return: Fundamental
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.lookup_fundamental_with_http_info(identifier, statement_code, fiscal_year, fiscal_period, **kwargs)  # noqa: E501
        else:
            (data) = self.lookup_fundamental_with_http_info(identifier, statement_code, fiscal_year, fiscal_period, **kwargs)  # noqa: E501
            return data

    def lookup_fundamental_with_http_info(self, identifier, statement_code, fiscal_year, fiscal_period, **kwargs):  # noqa: E501
        """Lookup Fundamental  # noqa: E501

        Returns the Fundamental for the Company with the given `identifier` and with the given parameters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.lookup_fundamental_with_http_info(identifier, statement_code, fiscal_year, fiscal_period, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: A Company identifier (Ticker, CIK, LEI, Intrinio ID) (required)
        :param str statement_code: The statement code (required)
        :param int fiscal_year: The fiscal year (required)
        :param str fiscal_period: The fiscal period (required)
        :return: Fundamental
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'statement_code', 'fiscal_year', 'fiscal_period']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lookup_fundamental" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `lookup_fundamental`")  # noqa: E501
        # verify the required parameter 'statement_code' is set
        if ('statement_code' not in params or
                params['statement_code'] is None):
            raise ValueError("Missing the required parameter `statement_code` when calling `lookup_fundamental`")  # noqa: E501
        # verify the required parameter 'fiscal_year' is set
        if ('fiscal_year' not in params or
                params['fiscal_year'] is None):
            raise ValueError("Missing the required parameter `fiscal_year` when calling `lookup_fundamental`")  # noqa: E501
        # verify the required parameter 'fiscal_period' is set
        if ('fiscal_period' not in params or
                params['fiscal_period'] is None):
            raise ValueError("Missing the required parameter `fiscal_period` when calling `lookup_fundamental`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'statement_code' in params:
            path_params['statement_code'] = params['statement_code']  # noqa: E501
        if 'fiscal_year' in params:
            path_params['fiscal_year'] = params['fiscal_year']  # noqa: E501
        if 'fiscal_period' in params:
            path_params['fiscal_period'] = params['fiscal_period']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/fundamentals/lookup/{identifier}/{statement_code}/{fiscal_year}/{fiscal_period}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Fundamental',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

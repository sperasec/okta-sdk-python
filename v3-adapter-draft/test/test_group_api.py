# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API  # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: devex-public@okta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.group_api import GroupApi  # noqa: E501
from swagger_client.rest import ApiException


class TestGroupApi(unittest.TestCase):
    """GroupApi unit test stubs"""

    def setUp(self):
        self.api = GroupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_activate_group_rule(self):
        """Test case for activate_group_rule

        Activate a group Rule  # noqa: E501
        """
        pass

    def test_add_application_instance_target_to_app_admin_role_given_to_group(self):
        """Test case for add_application_instance_target_to_app_admin_role_given_to_group

        Add App Instance Target to App Administrator Role given to a Group  # noqa: E501
        """
        pass

    def test_add_application_target_to_admin_role_given_to_group(self):
        """Test case for add_application_target_to_admin_role_given_to_group

        """
        pass

    def test_add_group_target_to_group_administrator_role_for_group(self):
        """Test case for add_group_target_to_group_administrator_role_for_group

        Add Group Target for Group Role  # noqa: E501
        """
        pass

    def test_add_user_to_group(self):
        """Test case for add_user_to_group

        Add User to Group  # noqa: E501
        """
        pass

    def test_assign_role_to_group(self):
        """Test case for assign_role_to_group

        """
        pass

    def test_create_group(self):
        """Test case for create_group

        Add Group  # noqa: E501
        """
        pass

    def test_create_group_rule(self):
        """Test case for create_group_rule

        Create Group Rule  # noqa: E501
        """
        pass

    def test_deactivate_group_rule(self):
        """Test case for deactivate_group_rule

        Deactivate a group Rule  # noqa: E501
        """
        pass

    def test_delete_group(self):
        """Test case for delete_group

        Remove Group  # noqa: E501
        """
        pass

    def test_delete_group_rule(self):
        """Test case for delete_group_rule

        Delete a group Rule  # noqa: E501
        """
        pass

    def test_get_group(self):
        """Test case for get_group

        List Group Rules  # noqa: E501
        """
        pass

    def test_get_group_rule(self):
        """Test case for get_group_rule

        Get Group Rule  # noqa: E501
        """
        pass

    def test_get_role(self):
        """Test case for get_role

        """
        pass

    def test_list_application_targets_for_application_administrator_role_for_group(self):
        """Test case for list_application_targets_for_application_administrator_role_for_group

        """
        pass

    def test_list_assigned_applications_for_group(self):
        """Test case for list_assigned_applications_for_group

        List Assigned Applications  # noqa: E501
        """
        pass

    def test_list_group_assigned_roles(self):
        """Test case for list_group_assigned_roles

        """
        pass

    def test_list_group_rules(self):
        """Test case for list_group_rules

        List Group Rules  # noqa: E501
        """
        pass

    def test_list_group_targets_for_group_role(self):
        """Test case for list_group_targets_for_group_role

        List Group Targets for Group Role  # noqa: E501
        """
        pass

    def test_list_group_users(self):
        """Test case for list_group_users

        List Group Members  # noqa: E501
        """
        pass

    def test_list_groups(self):
        """Test case for list_groups

        List Groups  # noqa: E501
        """
        pass

    def test_remove_application_target_from_administrator_role_given_to_group(self):
        """Test case for remove_application_target_from_administrator_role_given_to_group

        Remove App Instance Target to App Administrator Role given to a Group  # noqa: E501
        """
        pass

    def test_remove_application_target_from_application_administrator_role_given_to_group(self):
        """Test case for remove_application_target_from_application_administrator_role_given_to_group

        """
        pass

    def test_remove_group_target_from_group_administrator_role_given_to_group(self):
        """Test case for remove_group_target_from_group_administrator_role_given_to_group

        Delete Group Target for Group Role  # noqa: E501
        """
        pass

    def test_remove_role_from_group(self):
        """Test case for remove_role_from_group

        """
        pass

    def test_remove_user_from_group(self):
        """Test case for remove_user_from_group

        Remove User from Group  # noqa: E501
        """
        pass

    def test_update_group(self):
        """Test case for update_group

        Update Group  # noqa: E501
        """
        pass

    def test_update_group_rule(self):
        """Test case for update_group_rule

        """
        pass


if __name__ == '__main__':
    unittest.main()
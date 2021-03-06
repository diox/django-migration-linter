# Copyright 2019 3YOURMIND GmbH

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import shutil

_BASE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'tests/')
_FIXTURES_FOLDER = os.path.join(_BASE_DIR, 'test_project_fixtures/')

ADD_NOT_NULL_COLUMN_PROJECT = os.path.join(
    _FIXTURES_FOLDER, 'test_project_add_not_null_column/')
CREATE_TABLE_WITH_NOT_NULL_COLUMN_PROJECT = os.path.join(
    _FIXTURES_FOLDER, 'test_project_create_table_with_not_null_column/')
DROP_COLUMN_PROJECT = os.path.join(
    _FIXTURES_FOLDER, 'test_project_drop_column/')
RENAME_COLUMN_PROJECT = os.path.join(
    _FIXTURES_FOLDER, 'test_project_rename_column/')
ALTER_COLUMN_PROJECT = os.path.join(
    _FIXTURES_FOLDER, 'test_project_alter_column')
RENAME_TABLE_PROJECT = os.path.join(
    _FIXTURES_FOLDER, 'test_project_rename_table/')
ADD_NOT_NULL_COLUMN_FOLLOWED_BY_DEFAULT_PROJECT = os.path.join(
    _FIXTURES_FOLDER, 'test_project_add_not_null_column_followed_by_default/')
MULTI_COMMIT_PROJECT = os.path.join(
    _FIXTURES_FOLDER, 'test_project_multi_commit/')
CORRECT_PROJECT = os.path.join(
    _FIXTURES_FOLDER, 'test_correct_project/')
DELETED_MIGRATION_PROJECT = os.path.join(
    _FIXTURES_FOLDER, 'test_deleted_migration_project/')
IGNORE_MIGRATION_PROJECT = os.path.join(
    _FIXTURES_FOLDER, 'test_project_ignore_migration/')

NOT_DJANGO_GIT_PROJECT = os.path.join(
    _FIXTURES_FOLDER, 'test_git_project/')
NOT_GIT_DJANGO_PROJECT = os.path.join(
    _FIXTURES_FOLDER, 'test_django_without_git_project/')

NON_GIT_ROOT_GIT_FOLDER = os.path.join(
    _FIXTURES_FOLDER, 'test_non_root_git_project/'
)
NON_GIT_ROOT_DJANGO_PROJECT = os.path.join(
    NON_GIT_ROOT_GIT_FOLDER, 'django_project/'
)


ALL_GIT_PROJECTS = (
    NOT_DJANGO_GIT_PROJECT,
    MULTI_COMMIT_PROJECT,
    DELETED_MIGRATION_PROJECT,
    NON_GIT_ROOT_GIT_FOLDER,
)


def prepare_git_project(path):
    """Copy the git/ folder to .git/ so it is
    actually versioned"""
    src_git = os.path.join(path, 'git/')
    dest_git = os.path.join(path, '.git/')
    try:
        shutil.copytree(src_git, dest_git)
    except OSError:
        pass  # .git/ might already exist


def clear_all_git_projects():
    """Delete all .git/ folders in test projects"""
    for project_path in ALL_GIT_PROJECTS:
        git_path = os.path.join(project_path, '.git/')
        shutil.rmtree(git_path, ignore_errors=True)

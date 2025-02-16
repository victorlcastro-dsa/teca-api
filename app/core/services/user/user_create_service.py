from typing import Optional

from app.api.schemas.user_schema import UserInputSchema, UserOutputSchema
from app.common.hash_utils import hash_provider
from app.core.repositories.user.user_create_repository import UserCreateRepository
from app.core.repositories.user.user_get_repository import UserGetRepository
from app.core.services.shared.create_service import CreateService
from app.core.services.user.user_get_service import UserGetService


class UserCreateService(CreateService):
    """
    Service for managing user-related business logic.
    Handles creation of new users with role assignment and password hashing.
    """

    def __init__(self, repository: UserCreateRepository):
        """
        Initialize the service with a repository for user operations.

        Args:
            repository (UserCreateRepository): An instance of UserCreateRepository
                to handle data persistence for the User model.
        """
        super().__init__(repository)
        self._get_repository = UserGetRepository()
        self._get_service = UserGetService(self._get_repository)

    async def create(
        self,
        user_data: UserInputSchema,
    ) -> Optional[UserOutputSchema]:
        (
            """
        Create a new user with additional business logic.

        Args:
            name (str): The name of the user.
            email (str): The email of the user.
            password (str): The plain-text password to be hashed.
            roles (Optional[List[str]]): List of roles to assign to the user.

        Returns:
            UserOutputSchema: Serialized data of the created user.

        Raises:
            UserAlreadyExistsException: If a user with the given email
            already exists.
        """
            """
        Create a new user with additional business logic.

        Args:
            name (str): The name of the user.
            email (str): The email of the user.
            password (str): The plain-text password to be hashed.
            roles (Optional[List[str]]): List of roles to assign to the user.

        Returns:
            UserOutputSchema: Serialized data of the created user.

        Raises:
            UserAlreadyExistsException: If a user with the given email
            already exists.
        """
        )
        # roles = user.roles or ["user"]  # Assign default role if none provided

        # Check if a user with the email already exists
        # existing_user = await self._get_service.get_by_email(user_data.email)
        # if existing_user:
        #     raise UserAlreadyExistsException(
        #         f"User with email {user_data.email} already exists."
        #     )

        print(user_data)
        userValidated = user_data.validate(user_data)
        print(userValidated)
        password = userValidated.password.get_secret_value()
        userValidated.password_hash = hash_provider(password)

        created_user = await self.create_record(userValidated)
        # created_user = await self.create_record(user_data)
        return UserOutputSchema().validate(created_user)


# FIXME: Did not created the user, and raised: pydantic_core._pydantic_core.ValidationError: 4 validation error for UserOutputSchema

import { makeApi, Zodios, type ZodiosOptions } from "@zodios/core";
import { z } from "zod";

const UserCreate = z
  .object({ username: z.string(), email: z.string(), password: z.string() })
  .passthrough();
const User = z
  .object({
    username: z.string(),
    email: z.string(),
    id: z.union([z.number(), z.null()]),
    pass_hash: z.string(),
  })
  .passthrough();
const ValidationError = z
  .object({
    loc: z.array(z.union([z.string(), z.number()])),
    msg: z.string(),
    type: z.string(),
  })
  .passthrough();
const HTTPValidationError = z
  .object({ detail: z.array(ValidationError) })
  .partial()
  .passthrough();
const user_name = z.union([z.string(), z.null()]).optional();
const ReviewCreate = z
  .object({ content: z.string(), owner_id: z.number().int().optional() })
  .passthrough();
const Review = z
  .object({
    content: z.string(),
    owner_id: z.number().int().optional(),
    id: z.union([z.number(), z.null()]),
  })
  .passthrough();
const Body_generate_token_api_get_token_post = z
  .object({
    grant_type: z.union([z.string(), z.null()]).optional(),
    username: z.string(),
    password: z.string(),
    scope: z.string().optional(),
    client_id: z.union([z.string(), z.null()]).optional(),
    client_secret: z.union([z.string(), z.null()]).optional(),
  })
  .passthrough();
const Token = z
  .object({ access_token: z.string(), token_type: z.string() })
  .passthrough();
const Body_upload_book_api_upload_book__post = z
  .object({ file: z.instanceof(File) })
  .passthrough();
const Book = z
  .object({
    name: z.string(),
    description: z.string(),
    file_path: z.string(),
    id: z.union([z.number(), z.null()]),
  })
  .passthrough();

export const schemas = {
  UserCreate,
  User,
  ValidationError,
  HTTPValidationError,
  user_name,
  ReviewCreate,
  Review,
  Body_generate_token_api_get_token_post,
  Token,
  Body_upload_book_api_upload_book__post,
  Book,
};

const endpoints = makeApi([
  {
    method: "get",
    path: "/api",
    alias: "root",
    requestFormat: "json",
    response: z.string(),
  },
  {
    method: "get",
    path: "/api/files/",
    alias: "read_file",
    requestFormat: "json",
    parameters: [
      {
        name: "file_path",
        type: "Query",
        schema: z.string(),
      },
    ],
    response: z.unknown(),
    errors: [
      {
        status: 422,
        description: `Validation Error`,
        schema: HTTPValidationError,
      },
    ],
  },
  {
    method: "get",
    path: "/api/get-book/:id",
    alias: "get_book_by_id",
    requestFormat: "json",
    parameters: [
      {
        name: "id",
        type: "Path",
        schema: z.number().int(),
      },
    ],
    response: z.union([Book, z.null()]),
    errors: [
      {
        status: 422,
        description: `Validation Error`,
        schema: HTTPValidationError,
      },
    ],
  },
  {
    method: "post",
    path: "/api/get-token",
    alias: "generate_token",
    requestFormat: "form-url",
    parameters: [
      {
        name: "body",
        type: "Body",
        schema: Body_generate_token_api_get_token_post,
      },
    ],
    response: Token,
    errors: [
      {
        status: 422,
        description: `Validation Error`,
        schema: HTTPValidationError,
      },
    ],
  },
  {
    method: "post",
    path: "/api/review",
    alias: "create_review",
    requestFormat: "json",
    parameters: [
      {
        name: "body",
        type: "Body",
        schema: ReviewCreate,
      },
    ],
    response: Review,
    errors: [
      {
        status: 422,
        description: `Validation Error`,
        schema: HTTPValidationError,
      },
    ],
  },
  {
    method: "post",
    path: "/api/upload-book/",
    alias: "upload_book",
    requestFormat: "form-data",
    parameters: [
      {
        name: "body",
        type: "Body",
        schema: z.object({ file: z.instanceof(File) }).passthrough(),
      },
      {
        name: "name",
        type: "Query",
        schema: z.string(),
      },
      {
        name: "description",
        type: "Query",
        schema: z.string(),
      },
    ],
    response: Book,
    errors: [
      {
        status: 422,
        description: `Validation Error`,
        schema: HTTPValidationError,
      },
    ],
  },
  {
    method: "post",
    path: "/api/user",
    alias: "create_user",
    requestFormat: "json",
    parameters: [
      {
        name: "body",
        type: "Body",
        schema: UserCreate,
      },
    ],
    response: User,
    errors: [
      {
        status: 422,
        description: `Validation Error`,
        schema: HTTPValidationError,
      },
    ],
  },
  {
    method: "get",
    path: "/api/user/:user_id",
    alias: "get_user_by_id",
    requestFormat: "json",
    parameters: [
      {
        name: "user_id",
        type: "Path",
        schema: z.number().int(),
      },
    ],
    response: User,
    errors: [
      {
        status: 422,
        description: `Validation Error`,
        schema: HTTPValidationError,
      },
    ],
  },
  {
    method: "delete",
    path: "/api/user/:user_id",
    alias: "delete_user_by_id",
    requestFormat: "json",
    parameters: [
      {
        name: "user_id",
        type: "Path",
        schema: z.number().int(),
      },
    ],
    response: User,
    errors: [
      {
        status: 422,
        description: `Validation Error`,
        schema: HTTPValidationError,
      },
    ],
  },
  {
    method: "put",
    path: "/api/user/:user_id",
    alias: "update_user_by_id",
    requestFormat: "json",
    parameters: [
      {
        name: "body",
        type: "Body",
        schema: UserCreate,
      },
      {
        name: "user_id",
        type: "Path",
        schema: z.number().int(),
      },
    ],
    response: User,
    errors: [
      {
        status: 422,
        description: `Validation Error`,
        schema: HTTPValidationError,
      },
    ],
  },
  {
    method: "get",
    path: "/api/users",
    alias: "get_user_by_name",
    requestFormat: "json",
    parameters: [
      {
        name: "user_name",
        type: "Query",
        schema: user_name,
      },
    ],
    response: User,
    errors: [
      {
        status: 422,
        description: `Validation Error`,
        schema: HTTPValidationError,
      },
    ],
  },
  {
    method: "delete",
    path: "/api/users",
    alias: "delete_user_by_name",
    requestFormat: "json",
    parameters: [
      {
        name: "user_name",
        type: "Query",
        schema: user_name,
      },
    ],
    response: User,
    errors: [
      {
        status: 422,
        description: `Validation Error`,
        schema: HTTPValidationError,
      },
    ],
  },
  {
    method: "get",
    path: "/api/users/me",
    alias: "get_current_user",
    requestFormat: "json",
    response: z.union([User, z.null()]),
  },
]);

export const api = new Zodios(endpoints);

export function createApiClient(baseUrl: string, options?: ZodiosOptions) {
  return new Zodios(baseUrl, endpoints, options);
}

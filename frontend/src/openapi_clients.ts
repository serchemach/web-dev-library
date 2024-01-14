import { makeApi, Zodios } from "@zodios/core";
import { z } from "zod";

export const UserCreate = z
  .object({ username: z.string(), email: z.string(), password: z.string() })
  .passthrough();
export type UserCreate = z.infer<typeof UserCreate>;
export const User = z
  .object({
    username: z.string(),
    email: z.string(),
    id: z.union([z.number(), z.null()]),
    pass_hash: z.string(),
  })
  .passthrough();
export type User = z.infer<typeof User>;
export const ValidationError = z
  .object({
    loc: z.array(z.union([z.string(), z.number()])),
    msg: z.string(),
    type: z.string(),
  })
  .passthrough();
export type ValidationError = z.infer<typeof ValidationError>;
export const HTTPValidationError = z
  .object({ detail: z.array(ValidationError) })
  .partial()
  .passthrough();
export type HTTPValidationError = z.infer<typeof HTTPValidationError>;
export const user_name = z.union([z.string(), z.null()]).optional();
export type user_name = z.infer<typeof user_name>;
export const Body_generate_token_api_get_token_post = z
  .object({
    grant_type: z.union([z.string(), z.null()]).optional(),
    username: z.string(),
    password: z.string(),
    scope: z.string().optional(),
    client_id: z.union([z.string(), z.null()]).optional(),
    client_secret: z.union([z.string(), z.null()]).optional(),
  })
  .passthrough();
export type Body_generate_token_api_get_token_post = z.infer<
  typeof Body_generate_token_api_get_token_post
>;
export const Token = z
  .object({ access_token: z.string(), token_type: z.string() })
  .passthrough();
export type Token = z.infer<typeof Token>;
export const FavoriteBookLink = z
  .object({
    user_id: z.union([z.number(), z.null()]),
    book_id: z.union([z.number(), z.null()]),
  })
  .partial()
  .passthrough();
export type FavoriteBookLink = z.infer<typeof FavoriteBookLink>;
export const BookView = z
  .object({
    name: z.string(),
    description: z.string(),
    file_path: z.string(),
    preview_path: z.union([z.string(), z.null()]),
    id: z.number().int(),
    isFavorite: z.boolean(),
  })
  .passthrough();
export type BookView = z.infer<typeof BookView>;
export const Body_upload_book_api_upload_book__post = z
  .object({ file: z.instanceof(File) })
  .passthrough();
export type Body_upload_book_api_upload_book__post = z.infer<
  typeof Body_upload_book_api_upload_book__post
>;
export const Book = z
  .object({
    name: z.string(),
    description: z.string(),
    file_path: z.string(),
    preview_path: z.union([z.string(), z.null()]),
    id: z.union([z.number(), z.null()]),
  })
  .passthrough();
export type Book = z.infer<typeof Book>;
export const ReviewView = z
  .object({ content: z.string(), owner: User, book: Book })
  .passthrough();
export type ReviewView = z.infer<typeof ReviewView>;
export const BookViewReview = z
  .object({
    name: z.string(),
    description: z.string(),
    file_path: z.string(),
    preview_path: z.union([z.string(), z.null()]),
    id: z.number().int(),
    isFavorite: z.boolean(),
    reviews: z.array(ReviewView),
  })
  .passthrough();
export type BookViewReview = z.infer<typeof BookViewReview>;
export const ReviewCreate = z
  .object({ content: z.string(), book_id: z.number().int() })
  .passthrough();
export type ReviewCreate = z.infer<typeof ReviewCreate>;
export const Review = z
  .object({
    content: z.string(),
    owner_id: z.number().int().optional(),
    book_id: z.number().int().optional(),
    id: z.union([z.number(), z.null()]),
  })
  .passthrough();
export type Review = z.infer<typeof Review>;

export const schemas = {
  UserCreate,
  User,
  ValidationError,
  HTTPValidationError,
  user_name,
  Body_generate_token_api_get_token_post,
  Token,
  FavoriteBookLink,
  BookView,
  Body_upload_book_api_upload_book__post,
  Book,
  ReviewView,
  BookViewReview,
  ReviewCreate,
  Review,
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
    path: "/api/files/:file_path",
    alias: "read_file",
    requestFormat: "json",
    parameters: [
      {
        name: "file_path",
        type: "Path",
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
    path: "/api/get-book-full/:id",
    alias: "get_book_by_id_with_favorite_and_reviews",
    requestFormat: "json",
    parameters: [
      {
        name: "id",
        type: "Path",
        schema: z.number().int(),
      },
    ],
    response: BookViewReview,
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
    method: "get",
    path: "/api/get-books",
    alias: "get_books",
    requestFormat: "json",
    parameters: [
      {
        name: "offset",
        type: "Query",
        schema: z.number().int(),
      },
      {
        name: "limit",
        type: "Query",
        schema: z.number().int(),
      },
    ],
    response: z.array(BookView),
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
    path: "/api/get-reviews-book-id",
    alias: "get_reviews_by_book_id",
    requestFormat: "json",
    parameters: [
      {
        name: "book_id",
        type: "Query",
        schema: z.number().int(),
      },
    ],
    response: z.array(Review),
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
    method: "get",
    path: "/api/get-user-reviews",
    alias: "get_user_reviews",
    requestFormat: "json",
    response: z.array(ReviewView),
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
    path: "/api/users/add-favorite",
    alias: "add_favorite_book",
    requestFormat: "json",
    parameters: [
      {
        name: "book_id",
        type: "Query",
        schema: z.number().int(),
      },
    ],
    response: FavoriteBookLink,
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
    path: "/api/users/get-favorites",
    alias: "get_favorite_books",
    requestFormat: "json",
    response: z.array(BookView),
  },
  {
    method: "get",
    path: "/api/users/me",
    alias: "get_current_user",
    requestFormat: "json",
    response: z.union([User, z.null()]),
  },
  {
    method: "get",
    path: "/api/users/remove-favorite",
    alias: "remove_favorite_book",
    requestFormat: "json",
    parameters: [
      {
        name: "book_id",
        type: "Query",
        schema: z.number().int(),
      },
    ],
    response: FavoriteBookLink,
    errors: [
      {
        status: 422,
        description: `Validation Error`,
        schema: HTTPValidationError,
      },
    ],
  },
]);

export const api = new Zodios(endpoints);

export function createApiClient(baseUrl: string, options?: ZodiosOptions) {
  return new Zodios(baseUrl, endpoints, options);
}

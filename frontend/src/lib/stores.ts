import { writable } from "svelte/store";

// Get the value out of storage on load.
const stored = localStorage.apiToken
export const apiToken = writable(stored || "");
apiToken.subscribe((value) => localStorage.apiToken = value)

// export const userObj = writable();

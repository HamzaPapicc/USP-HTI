import { apiUrl } from "./apiUrl";
import { getCSRFToken } from "./csrf";

export async function apiFetch(path, options= {})
{
    const method = options.method?.toUpperCase() || "GET";

    const headers = {
        ...(options.headers || {})
    }

    if (!["GET", "HEAD", "OPTIONS"].includes(method))
    {
        const csrf = getCSRFToken();
        if (csrf)
        {
            headers["X-CSRFToken"] = csrf;
        }
    }

    let response = await fetch(apiUrl(path), {
        credentials: "include",
        ...options,
        headers
    });

    if (response.status === 401 && path !== "/api/token/refresh/")
    {
        const refresh = await fetch(apiUrl("/api/token/refresh/"), {
            method: "POST",
            credentials: "include",
            headers: {
                "X-CSRFToken": getCSRFToken()
            }
        });

        if (refresh.ok)
        {
            response = await fetch(apiUrl(path), {
                credentials: "include",
                ...options,
                headers
            });
        }
    }
    return response;
}
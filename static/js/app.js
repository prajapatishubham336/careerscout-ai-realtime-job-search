const form = document.getElementById("form"),
    input = document.getElementById("input"),
    chat = document.getElementById("chat"),
    loading = document.getElementById("loading");

let query = "",
    offset = 0;
function fill(x) {
    input.value = x;
    input.focus();}
function esc(s) {
    return String(s ?? "").replace(
        /[&<>"']/g,
        m => ({
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
            '"': "&quot;",
            "'": "&#039;"
        }[m])
    );
}

function cards(jobs) {
    return jobs.map(j => `
        <article class="job">
            <div class="top">
                <div>
                    <b>${esc(j.title)}</b>
                    <div class="company">
                        🏢 ${esc(j.company)}
                    </div>
                </div>

                <span class="pill">
                    ${esc(j.type)}
                </span>
            </div>

            <div class="meta">
                📍 ${esc(j.location)} · 🎓 ${esc(j.experience)}
            </div>

            <div class="skills">
                <b>Skills:</b> ${esc(j.skills)}
            </div>

            <div class="desc">
                ${esc(j.description)}
            </div>

            <a
                class="apply"
                href="${esc(j.apply_url)}"
                target="_blank"
                rel="noopener"
            >
                Apply Directly ↗
            </a>
        </article>
    `).join("");
}

function render(d, append = false) {
    document.querySelector(".more")?.remove();

    const block = `
        <div class="ai">
            ${esc(d.message)}
        </div>
        <div class="results">
            ${cards(d.jobs)}
        </div>

        ${
            d.has_more
                ? '<button class="more" onclick="more()">Show 10 more live opportunities →</button>'
                : ""
        }
    `;
    if (append) {
        chat.insertAdjacentHTML("beforeend", block);
    } else {
        chat.innerHTML = `
            <div class="user">
                ${esc(query)}
            </div>

            ${block}
        `;
    }
}

async function search() {
    query = input.value.trim();
    if (!query) return;
    offset = 0;
    loading.style.display = "block";

    try {
        const r = await fetch("/api/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: query,
                offset
            })
        });

        render(await r.json());
    } catch (e) {
        chat.innerHTML = `
            <div class="ai">
                Could not reach the server.
            </div>
        `;

    } finally {
        loading.style.display = "none";
    }
}

async function more() {
    offset += 10;
    loading.style.display = "block";
    try {
        const r = await fetch("/api/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: query,
                offset
            })
        });
        render(await r.json(), true);
    } finally {
        loading.style.display = "none";
    }
}

form.addEventListener("submit", e => {
    e.preventDefault();
    search();
});
let allPlayers = [];
let filteredPlayers = [];
let currentPage = 1;
const itemsPerPage = 20;
let currentFilter = "all";
let currentSort = { column: "cultivation", ascending: false };

function setHidden(id, hidden) {
    const el = document.getElementById(id);
    if (!el) return;
    el.classList.toggle("is-hidden", hidden);
}

async function loadData() {
    try {
        setHidden("loading", false);
        setHidden("error", true);
        setHidden("playersTable", true);
        setHidden("noData", true);

        const playersResponse = await fetch("/api/players");
        const playersData = await playersResponse.json();

        if (!playersData.success) {
            throw new Error(playersData.error || "加载失败");
        }

        allPlayers = playersData.players;
        filteredPlayers = [...allPlayers];

        const statsResponse = await fetch("/api/stats");
        const statsData = await statsResponse.json();

        if (statsData.success) {
            document.getElementById("totalPlayers").textContent = statsData.stats.total_players;
            document.getElementById("alivePlayers").textContent = statsData.stats.alive_players;
            document.getElementById("deadPlayers").textContent = statsData.stats.dead_players;
            document.getElementById("totalStones").textContent = statsData.stats.total_spirit_stones.toLocaleString();
        }

        setHidden("loading", true);
        document.getElementById("lastUpdate").textContent =
            "最后更新: " + new Date().toLocaleString("zh-CN");

        applyFilters();
        renderTable();
        loadQuests();
    } catch (error) {
        setHidden("loading", true);
        setHidden("error", false);
        document.getElementById("error").textContent = "加载失败: " + error.message;
    }
}

function applyFilters() {
    let result = [...allPlayers];

    if (currentFilter === "alive") {
        result = result.filter((p) => p.is_dead === 0);
    } else if (currentFilter === "dead") {
        result = result.filter((p) => p.is_dead === 1);
    }

    const searchTerm = document.getElementById("searchInput").value.toLowerCase();
    if (searchTerm) {
        result = result.filter(
            (p) =>
                p.name.toLowerCase().includes(searchTerm) ||
                p.realm.toLowerCase().includes(searchTerm) ||
                (p.sect && p.sect.toLowerCase().includes(searchTerm)) ||
                p.current_city.toLowerCase().includes(searchTerm)
        );
    }

    result.sort((a, b) => {
        let aVal = a[currentSort.column];
        let bVal = b[currentSort.column];

        if (aVal === null || aVal === undefined) aVal = "";
        if (bVal === null || bVal === undefined) bVal = "";

        if (typeof aVal === "string") {
            return currentSort.ascending
                ? aVal.localeCompare(bVal)
                : bVal.localeCompare(aVal);
        }
        return currentSort.ascending ? aVal - bVal : bVal - aVal;
    });

    filteredPlayers = result;
    currentPage = 1;
}

function renderTable() {
    const tbody = document.getElementById("playersBody");
    tbody.innerHTML = "";

    if (filteredPlayers.length === 0) {
        setHidden("playersTable", true);
        setHidden("noData", false);
        document.getElementById("pagination").innerHTML = "";
        return;
    }

    setHidden("playersTable", false);
    setHidden("noData", true);

    const start = (currentPage - 1) * itemsPerPage;
    const end = start + itemsPerPage;
    const pageData = filteredPlayers.slice(start, end);

    pageData.forEach((player) => {
        const row = document.createElement("tr");

        const statusClass = player.is_dead === 0 ? "alive" : "dead";
        const statusText = player.is_dead === 0 ? "健在" : "已坐化";

        row.innerHTML = `
            <td><strong>${player.name}</strong></td>
            <td>${player.gender}修</td>
            <td><span class="badge realm">${player.realm}</span></td>
            <td>${player.cultivation.toLocaleString()}</td>
            <td>${player.spirit_stones.toLocaleString()}</td>
            <td>${player.lifespan} / ${player.lifespan_max}</td>
            <td>${player.spirit_root}</td>
            <td>${player.sect || "-"}</td>
            <td>${player.cultivation_status || "-"}</td>
            <td>${player.cultivating_years_display || "-"}</td>
            <td>${player.retreat_remaining || "-"}</td>
            <td>${player.current_city}</td>
            <td><span class="badge ${statusClass}">${statusText}</span></td>
            <td>${player.last_active_formatted}</td>
        `;

        tbody.appendChild(row);
    });

    renderPagination();
}

function renderPagination() {
    const pagination = document.getElementById("pagination");
    pagination.innerHTML = "";

    const totalPages = Math.ceil(filteredPlayers.length / itemsPerPage);
    if (totalPages <= 1) return;

    const prevBtn = document.createElement("button");
    prevBtn.className = "page-btn";
    prevBtn.textContent = "← 上一页";
    prevBtn.disabled = currentPage === 1;
    prevBtn.addEventListener("click", () => {
        if (currentPage > 1) {
            currentPage--;
            renderTable();
        }
    });
    pagination.appendChild(prevBtn);

    const maxButtons = 7;
    let startPage = Math.max(1, currentPage - Math.floor(maxButtons / 2));
    let endPage = Math.min(totalPages, startPage + maxButtons - 1);

    if (endPage - startPage < maxButtons - 1) {
        startPage = Math.max(1, endPage - maxButtons + 1);
    }

    for (let i = startPage; i <= endPage; i++) {
        const btn = document.createElement("button");
        btn.className = "page-btn" + (i === currentPage ? " active" : "");
        btn.textContent = i;
        btn.addEventListener("click", () => {
            currentPage = i;
            renderTable();
        });
        pagination.appendChild(btn);
    }

    const nextBtn = document.createElement("button");
    nextBtn.className = "page-btn";
    nextBtn.textContent = "下一页 →";
    nextBtn.disabled = currentPage === totalPages;
    nextBtn.addEventListener("click", () => {
        if (currentPage < totalPages) {
            currentPage++;
            renderTable();
        }
    });
    pagination.appendChild(nextBtn);
}

function sortTable(column) {
    if (currentSort.column === column) {
        currentSort.ascending = !currentSort.ascending;
    } else {
        currentSort.column = column;
        currentSort.ascending = false;
    }

    applyFilters();
    renderTable();
}

function bindEvents() {
        document.getElementById("refreshBtn").addEventListener("click", () => {
            loadData();
            loadQuests();
        });

    document.getElementById("searchInput").addEventListener("input", () => {
        applyFilters();
        renderTable();
    });

    document.querySelectorAll(".filter-btn").forEach((btn) => {
        btn.addEventListener("click", function () {
            document.querySelectorAll(".filter-btn").forEach((b) => b.classList.remove("active"));
            this.classList.add("active");
            currentFilter = this.dataset.filter;
            applyFilters();
            renderTable();
        });
    });


    document.querySelectorAll("th[data-sort]").forEach((th) => {
        th.style.cursor = "pointer";
        th.addEventListener("click", () => {
            sortTable(th.dataset.sort);
        });
    });
}

document.addEventListener("DOMContentLoaded", () => {
    bindEvents();
    loadData();
    loadQuests();
    setInterval(() => {
        loadData();
        loadQuests();
    }, 30000);
});

async function loadQuests() {
    try {
        setHidden("questPanel", false);
        setHidden("questLoading", false);
        setHidden("questError", true);
        document.getElementById("questList").innerHTML = "";
        setHidden("noQuests", true);

        const response = await fetch("/api/quests");
        const data = await response.json();

        if (!data.success) {
            throw new Error(data.error || "加载任务失败");
        }

        setHidden("questLoading", true);

        document.getElementById("questCount").textContent = data.total;

        if (data.total === 0) {
            setHidden("noQuests", false);
            return;
        }

        renderQuests(data.quests);
    } catch (error) {
        setHidden("questLoading", true);
        setHidden("questError", false);
        document.getElementById("questError").textContent = "加载任务失败: " + error.message;
    }
}

function renderQuests(quests) {
    const questList = document.getElementById("questList");
    questList.innerHTML = "";

    quests.forEach((quest) => {
        const questItem = document.createElement("div");
        questItem.className = "quest-item" + (quest.is_complete ? " complete" : "");

        const typeLabel = quest.quest_type === "combat" ? "战斗" : quest.quest_type === "gather" ? "采集" : quest.quest_type;
        const typeClass = quest.quest_type === "combat" ? "combat" : "gather";
        const statusClass = quest.is_complete ? "complete" : "progress";

        questItem.innerHTML = `
            <div class="quest-item-header">
                <div>
                    <div class="quest-title">
                        ${quest.quest_title}
                        <span class="quest-type-badge ${typeClass}">${typeLabel}</span>
                    </div>
                    <div class="quest-player">👤 ${quest.player_name}</div>
                </div>
                <span class="quest-status ${statusClass}">${quest.status}</span>
            </div>
            <div class="quest-desc">${quest.quest_desc}</div>
            <div class="quest-time">
                <span>⏰ ${quest.quest_due_formatted}</span>
                <span>${quest.remaining_formatted}</span>
            </div>
        `;

        questList.appendChild(questItem);
    });
}

let allPlayers = [];
let filteredPlayers = [];
let currentPage = 1;
const itemsPerPage = 20;
let currentFilter = "all";
let currentSort = { column: "cultivation", ascending: false };
const sectionIds = ["home", "statistic", "player", "quest"];

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

        // Discovered sects

        let sects = Array.isArray(player.discovered_sects) && player.discovered_sects.length > 0
            ? `<div class='player-sects'>` + player.discovered_sects.map(s => `<span class='badge realm'>${s}</span>`).join(' ') + `</div>`
            : '-';

        let equipped = Array.isArray(player.techniques)
            ? `<div class='player-techniques'>` + player.techniques.filter(t => t.equipped).map(t =>
                `<span class='badge'>${t.name} <small>(${t.grade}, ${t.stage})</small></span>`
            ).join(' ') + `</div>` : '-';

        row.innerHTML = `
            <td data-label="姓名"><strong>${player.name}</strong></td>
            <td data-label="性别">${player.gender}修</td>
            <td data-label="境界"><span class="badge realm">${player.realm}</span></td>
            <td data-label="修为">${player.cultivation.toLocaleString()}</td>
            <td data-label="灵石">${player.spirit_stones.toLocaleString()}</td>
            <td data-label="寿元">${player.lifespan} / ${player.lifespan_max}</td>
            <td data-label="灵根">${player.spirit_root}</td>
            <td data-label="宗门">${player.sect || "-"}</td>
            <td data-label="修炼状态">${player.cultivation_status || "-"}</td>
            <td data-label="闭关设定">${player.cultivating_years_display || "-"}</td>
            <td data-label="闭关剩余">${player.retreat_remaining || "-"}</td>
            <td data-label="所在城市">${player.current_city}</td>
            <td data-label="状态"><span class="badge ${statusClass}">${statusText}</span></td>
            <td data-label="最后活跃">${player.last_active_formatted}</td>
            <td data-label="发现宗门">${sects}</td>
            <td data-label="装备功法">${equipped}</td>
            <td data-label="探险次数">${player.explore_count || 0}</td>
            <td data-label="最近探险城市">${player.current_city || '-'}</td>
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

function activateNav(targetId) {
    document.querySelectorAll(".nav-link").forEach((link) => {
        link.classList.toggle("active", link.dataset.target === targetId);
    });
}

function showSection(targetId) {
    const safeTargetId = sectionIds.includes(targetId) ? targetId : "home";

    sectionIds.forEach((sectionId) => {
        const sectionEl = document.getElementById(sectionId);
        if (!sectionEl) return;
        sectionEl.classList.toggle("is-active", sectionId === safeTargetId);
    });

    activateNav(safeTargetId);
}

function setupNavigation() {
    const navLinks = document.querySelectorAll(".nav-link");

    navLinks.forEach((link) => {
        link.addEventListener("click", (event) => {
            event.preventDefault();
            const targetId = link.dataset.target;
            showSection(targetId);

            if (targetId === "quest") {
                loadPublicEvents();
            }

            window.history.replaceState(null, "", `#${targetId}`);
        });
    });

    const hashTarget = window.location.hash.replace("#", "");
    showSection(hashTarget || "home");
}

document.addEventListener("DOMContentLoaded", () => {
    // PWA install prompt logic
    let deferredPrompt = null;
    const installBtn = document.getElementById("installPwaBtn");
    window.addEventListener("beforeinstallprompt", (e) => {
        e.preventDefault();
        deferredPrompt = e;
        if (installBtn) installBtn.style.display = "inline-block";
    });
    if (installBtn) {
        installBtn.addEventListener("click", async () => {
            if (deferredPrompt) {
                deferredPrompt.prompt();
                const choiceResult = await deferredPrompt.userChoice;
                if (choiceResult.outcome === "accepted") {
                    installBtn.style.display = "none";
                }
                deferredPrompt = null;
            }
        });
    }
    setupNavigation();
    bindEvents();
    loadData();
    loadPublicEvents();
    setInterval(() => {
        loadData();
        loadPublicEvents();
    }, 30000);
});

async function loadPublicEvents() {
    try {
        setHidden("publicEventsPanel", false);
        setHidden("publicEventsLoading", false);
        setHidden("publicEventsError", true);
        document.getElementById("publicEventsList").innerHTML = "";
        setHidden("noPublicEvents", true);

        const response = await fetch("/api/public_events");
        const data = await response.json();

        if (!data.success) {
            throw new Error(data.error || "加载事件失败");
        }

        setHidden("publicEventsLoading", true);
        document.getElementById("publicEventsCount").textContent = data.total;

        if (data.total === 0) {
            setHidden("noPublicEvents", false);
            return;
        }

        renderPublicEvents(data.events);
    } catch (error) {
        setHidden("publicEventsLoading", true);
        setHidden("publicEventsError", false);
        document.getElementById("publicEventsError").textContent = "加载事件失败: " + error.message;
    }
}

function renderPublicEvents(events) {
    const eventsList = document.getElementById("publicEventsList");
    eventsList.innerHTML = "";

    events.forEach((event) => {
        const eventItem = document.createElement("div");
        eventItem.className = "event-item";

        // Participants rendering
        let participantsHtml = "<div class='event-participants'><strong>参与者:</strong>";
        if (event.participants && event.participants.length > 0) {
            participantsHtml += "<ul>";
            event.participants.forEach(p => {
                participantsHtml += `<li>
                    <span class='participant-id'>🆔 ${p.discord_id}</span>
                    <span class='participant-time'>加入: ${new Date(p.joined_at * 1000).toLocaleString("zh-CN")}</span>
                    <span class='participant-contribution'>贡献: ${p.contribution}</span>
                </li>`;
            });
            participantsHtml += "</ul>";
        } else {
            participantsHtml += " 无";
        }
        participantsHtml += "</div>";

        eventItem.innerHTML = `
            <div class="event-item-header">
                <div>
                    <div class="event-title">
                        ${event.title}
                        <span class="event-type-badge">${event.event_type}</span>
                    </div>
                </div>
                <span class="event-status">${event.status}</span>
            </div>
            <div class="event-time">
                <span>开始: ${new Date(event.started_at * 1000).toLocaleString("zh-CN")}</span>
                <span>结束: ${new Date(event.ends_at * 1000).toLocaleString("zh-CN")}</span>
            </div>
            <div class="event-data">${event.data}</div>
            ${participantsHtml}
        `;
        eventsList.appendChild(eventItem);
    });
}

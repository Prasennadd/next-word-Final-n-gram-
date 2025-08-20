document.addEventListener('DOMContentLoaded', () => {
    const inputBox = document.getElementById('inputBox');
    const suggestionsDiv = document.getElementById('suggestions');

    inputBox.addEventListener('input', async () => {
        const query = inputBox.value.trim();
        if (!query) {
            suggestionsDiv.innerHTML = '';
            return;
        }

        try {
            const res = await fetch(`/suggest?q=${encodeURIComponent(query)}`);
            const suggestions = await res.json();

            suggestionsDiv.innerHTML = '';
            suggestions.forEach(word => {
                const div = document.createElement('div');
                div.textContent = word;
                div.className = 'suggestion-item';
                div.onclick = () => {
                    inputBox.value = word;
                    suggestionsDiv.innerHTML = '';
                    inputBox.focus();
                };
                suggestionsDiv.appendChild(div);
            });
        } catch (error) {
            console.error('Error fetching suggestions:', error);
        }
    });
});

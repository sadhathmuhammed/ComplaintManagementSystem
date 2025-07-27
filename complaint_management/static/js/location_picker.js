document.addEventListener('DOMContentLoaded', function () {
    const pickLocationBtn = document.getElementById('pickLocationBtn');
    const locationInput = document.getElementById('location_field');
    const mapPopup = document.getElementById('mapPopup');
    const closeBtn = document.getElementById('closeMapBtn');
    const mapDiv = document.getElementById('map');

    let map = null;
    let marker = null;

    if (!pickLocationBtn || !locationInput || !mapPopup) return;

    pickLocationBtn.addEventListener('click', function () {
        // Show popup
        mapPopup.style.display = 'block';

        if (!map) {
            // Initialize map
            map = L.map(mapDiv).setView([20.5937, 78.9629], 5);

            // Add tile layer
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 18,
            }).addTo(map);

            // Click event on map
            map.on('click', function (e) {
                const lat = e.latlng.lat.toFixed(6);
                const lng = e.latlng.lng.toFixed(6);
                locationInput.value = `${lat}, ${lng}`;

                // Add/Move marker
                if (marker) {
                    marker.setLatLng(e.latlng);
                } else {
                    marker = L.marker(e.latlng).addTo(map);
                }

                // Close popup after selection
                mapPopup.style.display = 'none';
            });
        } else {
            // Fix rendering when popup is shown
            setTimeout(() => {
                map.invalidateSize();
            }, 300);
        }
    });

    // Close button
    closeBtn.addEventListener('click', function () {
        mapPopup.style.display = 'none';
    });
});

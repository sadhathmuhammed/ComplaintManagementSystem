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
        mapPopup.style.display = 'block';

        if (!map) {
            map = L.map(mapDiv).setView([20.5937, 78.9629], 5);

            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 18,
            }).addTo(map);

            map.on('click', function (e) {
                const lat = e.latlng.lat.toFixed(6);
                const lng = e.latlng.lng.toFixed(6);
                locationInput.value = `${lat}, ${lng}`;

                if (marker) {
                    marker.setLatLng(e.latlng);
                } else {
                    marker = L.marker(e.latlng).addTo(map);
                }

                mapPopup.style.display = 'none';
            });
        } else {
            setTimeout(() => {
                map.invalidateSize();
            }, 300);
        }
    });

    closeBtn.addEventListener('click', function () {
        mapPopup.style.display = 'none';
    });
});

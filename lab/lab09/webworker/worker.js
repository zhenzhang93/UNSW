const API_URL =
  'https://api.thecatapi.com/v1/images/search?&mime_types=image/gif';

const fetchImageMetaData = url => fetch(url).then(res => res.json());

const ready = data => {
  console.log(data);
  self.postMessage(data);
};

self.addEventListener('message', () => {
  fetchImageMetaData(API_URL)
    .then(([data]) => data)
    .then(ready);
});
const videoElement = document.getElementById('camera-feed');
let isHandOpenDetected = false;
let isHandCloseTriggered = false; // To prevent multiple triggers
let handCloseTimeout = null; // To store the timeout reference


// Initialize the camera
const camera = new Camera(videoElement, {
  onFrame: async () => {
      await hands.send({ image: videoElement });
  },
  width: 1280,
  height: 720
});
camera.start();

// Function to stop the camera feed
function stopCamera(videoElement) {
  const stream = videoElement.srcObject;
  if (stream) {
      const tracks = stream.getTracks();
      tracks.forEach(track => track.stop()); // Stop all tracks (video/audio)
      videoElement.srcObject = null; // Clear the video source
  }
}

// hand congif
const hands = new Hands({ locateFile: (file) => `https://cdn.jsdelivr.net/npm/@mediapipe/hands@0.1/${file}` });
hands.setOptions({
    maxNumHands: 1,
    modelComplexity: 1,
    minDetectionConfidence: 0.5,
    minTrackingConfidence: 0.5
});
hands.onResults(onResultsHands);


// detect hand close
function detectClose(lms) {
  const fingers = [8, 12, 16, 20];
  let close = true;

  for (let i = 0; i < fingers.length; i++) {
      const point = fingers[i];
      if (lms[point]['z'] < lms[point - 2]['z']) {
          close = false;
          break;
      }
  }
  return close;
}

// hand close trigger
function handCloseTriggered() {
  isHandCloseTriggered = true; // Prevent re-triggering
  console.log('Hand closed detected! Triggering actions...');
  const imageName = displayImage.src.split('/').pop();
  stopCamera(videoElement)
  shareImage(imageName)
  displayImage.style.height = '90vh'
  displayImage.style.opacity = '0.7'
}

// share IMage
function shareImage(imageName) {
  const data = { imageName: imageName };

  fetch('/get-user-ip/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'X-CSRFToken': '{{ csrf_token }}' },
      body: JSON.stringify(data)
  }).then(response => response.json())
    .then(result => console.log("Image shared:", result))
    .catch(error => console.error("Error sharing image:", error));
}


// runs on hand detection 
function onResultsHands(results) {
  if (results.multiHandLandmarks && results.multiHandedness) {

    const landmarks = results.multiHandLandmarks[0];

    performOPeration(landmarks,results)

  }
}

// detect hand open
function detectOpenHand(lms) {
  const fingers = [8, 12, 16, 20];
  let open = true;

  for (let i = 0; i < fingers.length; i++) {
      const point = fingers[i];
      if (lms[point]['z'] > lms[point - 2]['z']) { 
          open = false;
          break;
      }
  }

  return open;
}

// fetch image on receive
function checkImageFromDatabase() {
  fetch('/check-image/')
  .then(response => response.json())
  .then(data => {
      if (data.image_name) {
          imageContainer.innerHTML = `<img id="shared-image" src="/media/images/${data.image_name}" alt="Shared Image" style="opacity: 0;">`;
          const imgElement = document.getElementById('shared-image');

          imgElement.onload = () => {
              imgElement.style.opacity = '1';
              imgElement.classList.add('image-loaded'); 
          };
          stopCamera(videoElement)
      } else {
          console.log('No image found for this IP.');
      }
  })
  .catch(error => console.error('Error:', error));
}
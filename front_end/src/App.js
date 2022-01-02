import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition'
import { Container, Typography, Button } from '@mui/material'
import { useState } from 'react'


function App() {
  const [question, setQuestion] = useState([])

  const {
    transcript,
    listening,
    browserSupportsSpeechRecognition,
    resetTranscript
  } = useSpeechRecognition();

  const startListening = async () => {
    await SpeechRecognition.startListening({ continuous: true });
    resetTranscript()
  };

  const stopListening = async () => {
    console.log("listening "+transcript)
    SpeechRecognition.stopListening()
    let currQuestion = transcript
    resetTranscript()
    const data = await fetch(`http://127.0.0.1:8000/?question="${currQuestion}"`).then(res=>res.json())
    setQuestion([...question, currQuestion, data['answer']])
  }
  if (!browserSupportsSpeechRecognition) {
    return <span>Browser doesn't support speech recognition.</span>;
  }

  return (
    <Container>
      <Typography variant="h6">Microphone: {listening ? 'on' : 'off'}</Typography>
      <Button variant="contained"
        onTouchStart={startListening}
        onMouseDown={startListening}
        onTouchEnd={stopListening}
        onMouseUp={stopListening}
      >Hold to talk</Button>
      <Typography variant="h6">{transcript}</Typography>
      {question.map((a, index) => (
        <Typography key={index} variant="h6">{a}</Typography>
      ))} 
    </Container>
  )
}

export default App;
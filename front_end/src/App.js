import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition'
import { Container, Typography, Button } from '@mui/material'
import { useState } from 'react'
import BasicCard from './components/BasicCard'

function App() {
  const [questions, setQuestions] = useState([])

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
    setQuestions([...questions, {bot: 0, content: currQuestion}, {bot: 1, content:data['answer']}])
  }
  if (!browserSupportsSpeechRecognition) {
    return <span>Browser doesn't support speech recognition.</span>;
  }

  return (
    <Container>
      <Typography variant="h6"  sx={{mb: 1}}>{listening ? 'I\'m hearing....' : 'Hi, my name is Hannah.'}</Typography>
      <Button variant="contained"
        onTouchStart={startListening}
        onMouseDown={startListening}
        onTouchEnd={stopListening}
        onMouseUp={stopListening}
        sx={{mb: 2}}
      >Hold to talk</Button>
      <BasicCard user={`Question: ` + transcript}></BasicCard>
      {questions.map((question) => {
        if (question.content !== "\n\n" && question.content.length !== 0) {
          return question.bot === 0 
          ? <BasicCard user="User" content={question.content} color="error.main"></BasicCard>
          : <BasicCard user="Hannad" content={question.content} color="green"></BasicCard>
      }})} 
    </Container>
  )
}

export default App
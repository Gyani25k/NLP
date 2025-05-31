import React from 'react';
import { Container, Box, Typography } from '@mui/material';

function App() {
  return (
    <Container maxWidth="sm">
      <Box sx={{ my: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>
          NLP Analysis System
        </Typography>
        <Typography variant="body1">
          This application allows users to perform NLP on both structured and unstructured data.
        </Typography>
      </Box>
    </Container>
  );
}

export default App;

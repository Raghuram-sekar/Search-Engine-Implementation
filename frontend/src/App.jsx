import React, { useState, useEffect } from 'react';
import {
  AppBar, Toolbar, Typography, Container, TextField, Card, CardContent, IconButton, Box, CssBaseline, createTheme, ThemeProvider, Pagination, Tooltip, Paper, useMediaQuery
} from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import Brightness4Icon from '@mui/icons-material/Brightness4';
import Brightness7Icon from '@mui/icons-material/Brightness7';
import PublicIcon from '@mui/icons-material/Public';

function highlightText(text, query) {
  if (!query) return text;
  const words = query.trim().split(/\s+/).filter(Boolean);
  if (words.length === 0) return text;
  const regex = new RegExp(`(${words.map(w => w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|')})`, 'gi');
  const parts = text.split(regex);
  return parts.map((part, i) =>
    regex.test(part) ? (
      <mark key={i} style={{ background: '#ffe066', padding: 0 }}>{part}</mark>
    ) : (
      <React.Fragment key={i}>{part}</React.Fragment>
    )
  );
}

function getDomain(url) {
  try {
    return new URL(url).hostname.replace(/^www\./, '');
  } catch {
    return url;
  }
}

const RESULTS_PER_PAGE = 5;

function App() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [page, setPage] = useState(1);
  const [mode, setMode] = useState(() => localStorage.getItem('mui-theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'));
  const isMobile = useMediaQuery('(max-width:600px)');

  const theme = React.useMemo(() => createTheme({
    palette: {
      mode,
      primary: { main: mode === 'dark' ? '#90caf9' : '#1976d2' },
      background: {
        default: mode === 'dark' ? '#181a1b' : 'linear-gradient(135deg, #e3f0ff 0%, #f9f9f9 100%)',
        paper: mode === 'dark' ? '#23272e' : '#fff',
      },
    },
    shape: { borderRadius: 16 },
    typography: { fontFamily: 'Inter, Roboto, Arial, sans-serif' },
  }), [mode]);

  useEffect(() => {
    localStorage.setItem('mui-theme', mode);
  }, [mode]);

  const handleSearch = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResults([]);
    setPage(1);
    try {
      const res = await fetch(`http://localhost:8000/search?q=${encodeURIComponent(query)}`);
      if (!res.ok) throw new Error('API error');
      const data = await res.json();
      setResults(data.results);
    } catch (err) {
      setError('Failed to fetch results. Is the backend running?');
    } finally {
      setLoading(false);
    }
  };

  const totalPages = Math.max(1, Math.ceil(results.length / RESULTS_PER_PAGE));
  const paginatedResults = results.slice((page - 1) * RESULTS_PER_PAGE, page * RESULTS_PER_PAGE);

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Box
        sx={{
          minHeight: '100vh',
          width: '100vw',
          background: mode === 'dark'
            ? theme.palette.background.default
            : 'linear-gradient(135deg, #e3f0ff 0%, #f9f9f9 100%)',
          display: 'flex',
          flexDirection: 'column',
        }}
      >
        <AppBar position="static" color="primary" elevation={2}>
          <Toolbar>
            <PublicIcon sx={{ mr: 1, fontSize: 32 }} />
            <Typography variant="h6" sx={{ flexGrow: 1, fontWeight: 700, letterSpacing: 1 }}>
              Modern Search Engine
            </Typography>
            <Tooltip title={mode === 'dark' ? 'Switch to light mode' : 'Switch to dark mode'}>
              <IconButton color="inherit" onClick={() => setMode(m => m === 'dark' ? 'light' : 'dark')}>
                {mode === 'dark' ? <Brightness7Icon /> : <Brightness4Icon />}
              </IconButton>
            </Tooltip>
          </Toolbar>
        </AppBar>
        <Box
          sx={{
            flex: 1,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            minHeight: '80vh',
            px: 2,
          }}
        >
          <Paper
            elevation={6}
            sx={{
              width: isMobile ? '100%' : 500,
              maxWidth: '100%',
              p: isMobile ? 2 : 4,
              borderRadius: 4,
              boxShadow: mode === 'dark' ? 8 : 4,
              background: mode === 'dark' ? theme.palette.background.paper : '#fff',
              transition: 'background 0.3s',
            }}
          >
            <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', mb: 2 }}>
              <PublicIcon sx={{ fontSize: 56, color: theme.palette.primary.main, mb: 1 }} />
              <Typography variant="h4" sx={{ fontWeight: 700, mb: 1, color: theme.palette.primary.main, letterSpacing: 1 }}>
                Search the Web
              </Typography>
            </Box>
            <Box component="form" onSubmit={handleSearch} sx={{ display: 'flex', gap: 2, mb: 3 }}>
              <TextField
                fullWidth
                variant="outlined"
                label="Search"
                value={query}
                onChange={e => setQuery(e.target.value)}
                autoFocus
                InputProps={{
                  endAdornment: (
                    <IconButton type="submit" color="primary" disabled={loading}>
                      <SearchIcon />
                    </IconButton>
                  ),
                }}
              />
            </Box>
            {error && <Typography color="error" sx={{ mb: 2 }}>{error}</Typography>}
            {paginatedResults.length > 0 && (
              <>
                {paginatedResults.map((r, i) => (
                  <Card key={i} sx={{ mb: 3, background: theme.palette.background.paper, boxShadow: 3 }}>
                    <CardContent>
                      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 0.5 }}>
                        <Typography variant="h6" component="a" href={r.url} target="_blank" rel="noopener noreferrer" sx={{ color: theme.palette.primary.main, fontWeight: 700, textDecoration: 'none', mr: 1 }}>
                          {r.title}
                        </Typography>
                        <Typography variant="body2" color="text.secondary">({getDomain(r.url)})</Typography>
                      </Box>
                      <Typography variant="body1" sx={{ color: theme.palette.text.primary, mb: 1, fontSize: 16 }}>
                        {highlightText(r.snippet, query)}
                      </Typography>
                      <Typography variant="body2" color="text.secondary" sx={{ wordBreak: 'break-all' }}>{r.url}</Typography>
                      <Typography variant="caption" color="text.secondary">
                        TF-IDF: {r.tfidf?.toFixed(3)} | PageRank: {r.pagerank?.toExponential(2)}
                        {r.crawled_at && (
                          <span style={{ marginLeft: 10 }}>
                            | Crawled: {new Date(r.crawled_at).toLocaleString()}
                          </span>
                        )}
                      </Typography>
                    </CardContent>
                  </Card>
                ))}
                <Box sx={{ display: 'flex', justifyContent: 'center', mt: 2 }}>
                  <Pagination
                    count={totalPages}
                    page={page}
                    onChange={(_, value) => setPage(value)}
                    color="primary"
                    shape="rounded"
                    size="large"
                    showFirstButton
                    showLastButton
                  />
                </Box>
              </>
            )}
          </Paper>
        </Box>
        <Box sx={{ textAlign: 'center', color: 'text.secondary', pb: 3 }}>
          Powered by FastAPI + React + Material UI
        </Box>
      </Box>
    </ThemeProvider>
  );
}

export default App;

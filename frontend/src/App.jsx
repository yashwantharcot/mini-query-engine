import React, { useState } from 'react';

const API_BASE_URL = '';
const API_KEY = 'secure_api_key_123';

const headers = {
  'Content-Type': 'application/json',
  'api-key': API_KEY,
};

function App() {
  const [query, setQuery] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [queryId, setQueryId] = useState(1);
  const [explanation, setExplanation] = useState('');
  const [validation, setValidation] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!query.trim()) return;

    setLoading(true);
    setError('');
    setResult(null);

    try {
      const response = await fetch(`${API_BASE_URL}/query`, {
        method: 'POST',
        headers,
        body: JSON.stringify({ natural_language_query: query }),
      });

      if (!response.ok) throw new Error('Failed to process query');
      const data = await response.json();
      setResult(data.pseudo_sql_query);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleExplain = async () => {
    setExplanation('Loading...');
    try {
      const response = await fetch(`${API_BASE_URL}/explain/${queryId}`, { headers });
      if (!response.ok) throw new Error('Query not found');
      const data = await response.json();
      setExplanation(data.explanation);
    } catch (err) {
      setExplanation(`Error: ${err.message}`);
    }
  };

  const handleValidate = async () => {
    setValidation('Validating...');
    try {
      const response = await fetch(`${API_BASE_URL}/validate/${queryId}`, { headers });
      if (!response.ok) throw new Error('Query not found');
      const data = await response.json();
      setValidation(data.validation);
    } catch (err) {
      setValidation(`Error: ${err.message}`);
    }
  };

  return (
    <div className="app-container">
      <header>
        <h1>Mini Query Engine</h1>
        <p className="subtitle">Transform natural language into SQL simulations instantly.</p>
      </header>

      <main>
        <div className="card">
          <label>Natural Language Query</label>
          <textarea
            rows="4"
            placeholder="e.g., Show me all users who signed up last week"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
          <div style={{ marginTop: '1.5rem', display: 'flex', gap: '1rem', alignItems: 'center' }}>
            <button onClick={handleSubmit} disabled={loading || !query.trim()}>
              {loading ? 'Processing...' : 'Generate SQL'}
            </button>
            {result && <span className="status-badge">Success</span>}
          </div>
          {error && <p className="error-message">{error}</p>}

          {result && (
            <div className="result-box">
              <label>Generated Pseudo-SQL</label>
              <pre><code>{result}</code></pre>
            </div>
          )}
        </div>

        <div className="grid">
          <div className="card">
            <div className="input-group">
              <label>Query ID</label>
              <input
                type="number"
                min="1"
                value={queryId}
                onChange={(e) => setQueryId(parseInt(e.target.value) || 1)}
              />
            </div>
            <div style={{ display: 'flex', gap: '1rem' }}>
              <button 
                onClick={handleExplain} 
                style={{ background: 'transparent', border: '1px solid var(--primary)', color: 'var(--primary)' }}
              >
                Explain
              </button>
              <button 
                onClick={handleValidate}
                style={{ background: 'transparent', border: '1px solid var(--accent)', color: 'var(--accent)' }}
              >
                Validate
              </button>
            </div>
          </div>

          <div className="card">
            <label>Details & Insights</label>
            {explanation && (
              <div style={{ marginBottom: '1rem' }}>
                <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem' }}>Explanation:</p>
                <p style={{ color: 'var(--text-main)', marginTop: '0.25rem' }}>{explanation}</p>
              </div>
            )}
            {validation && (
              <div>
                <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem' }}>Validation:</p>
                <p style={{ color: 'var(--accent)', marginTop: '0.25rem' }}>{validation}</p>
              </div>
            )}
            {!explanation && !validation && (
              <p style={{ color: 'var(--text-muted)', fontStyle: 'italic' }}>
                Enter a Query ID to see insights.
              </p>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;

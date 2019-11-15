import * as React from 'react';
import { Router, Link } from '@reach/router';
import { AppBar, IconButton, Toolbar } from '@material-ui/core';
import HomeIcon from '@material-ui/icons/Home';
import { ThemeProvider } from '@material-ui/styles';

import theme from './theme';
import Empty from './components/Empty';
import MeetingCardTest from './components/MeetingCardTest';

const App: React.SFC = function App() {
  return (
    <div>
      <ThemeProvider theme={theme}>
        <AppBar position="static">
          <Toolbar>
            <IconButton edge="start">
              <Link to="/">
                <HomeIcon color="secondary" />
              </Link>
            </IconButton>
          </Toolbar>
        </AppBar>
        <MeetingCardTest />
        <Router>
          {/* One component for each page/route goes in here */}
          <Empty path="/" />
          <Schedule path="/schedule" schedule={[testMeeting]} />
        </Router>
      </ThemeProvider>
    </div>
  );
};

export default App;

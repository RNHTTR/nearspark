import React, { useState } from 'react';
import { 
  Button,
  ButtonGroup,
  ButtonToolbar,
  ToggleButton,
  ToggleButtonGroup
} from 'react-bootstrap'

export function QueryButtonToolbar() {
  // const [checked, setChecked] = useState(false);
  const [radioValue, setRadioValue] = useState('1');

  const radios = [
    { name: 'Results', value: '1' },
    { name: 'Visualize', value: '2' },
  ];

  return (
    <>
      <ButtonToolbar className="mb-3 justify-content-between" aria-label="Toolbar with Button groups">
        <ToggleButtonGroup type="radio" name="options" defaultValue={1}>
          <ToggleButton id="results" value={1} variant="outline-secondary">View Results</ToggleButton>
          <ToggleButton id="visualize" value={2} variant="outline-secondary">Visualize Results</ToggleButton>
        </ToggleButtonGroup>
        <Button variant="primary">Run</Button>
      </ButtonToolbar>
    </>
  );
  }

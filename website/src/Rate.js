import React from 'react';
import { Button, Form, FormGroup, Label } from 'reactstrap';

export class Rate extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <Form>
            <FormGroup>
                <Label>Source</Label>
                <select name="source">
                    <option value="EUR">EUR</option>
                    <option value="GBP">GBP</option>
                    <option value="NZD">NZD</option>
                </select>
            </FormGroup>
            <FormGroup>
                <Label>Target</Label>
                <select name="target">
                    <option value="EUR">EUR</option>
                    <option value="GBP">GBP</option>
                    <option value="NZD">NZD</option>
                </select>
            </FormGroup>

            <FormGroup>
                <Button>Calculate</Button>
            </FormGroup>
        </Form>
      </div>
    )
  }
}
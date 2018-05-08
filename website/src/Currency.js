import React from 'react';
import { Button, Form, FormGroup, Label, Input, Col } from 'reactstrap';

export function Currency(props) {
    const name = "rate" + props.name
    return (
        <FormGroup row>
            <Label for={name} sm={4}>{props.name}</Label>
            <Col sm={2}>
                <Input type="select" name={props.field} id={name} defaultValue={props.default || 'EUR'} onChange={(e) => props.handleCurrency(e, props.field)}>
                    <option>EUR</option>
                    <option>GBP</option>
                    <option>NZD</option>
                </Input>
            </Col>
        </FormGroup>
    )
}
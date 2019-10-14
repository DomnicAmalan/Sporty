import React from 'react';

export class Redirect extends React.Component{
    componentDidMount(){
        setTimeout((time) => { 
            window.location = this.props.redirect_url
        }, this.props.timeout)
    }

    render(){
        return(
            <div>
               {this.props.message}
            </div>
        )
    }
}


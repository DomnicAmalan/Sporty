import React from 'react'
import ReactDOM from 'react-dom'
import Axios from 'axios';


class Dashboard extends React.Component {

    constructor(props){
        super(props);
        this.state = {}
    }

    UNSAFE_componentWillMount(){
        this.setState({
            all_sports: [],
            selected_sports: []
        })
    }

    componentDidMount(){
        Axios.get('/api/list/sports/all').then(res => {
            let data = res.data
            this.setState({
                all_sports: data
            })
        })
    }



    render() {

        let sports = []
        this.state.all_sports.forEach(sport => {
            sports.push(
                <div>{sport.name}</div>
            )
        });

        return (
           <div>
               Dashbaord
           </div>
        );
    }
  }

  ReactDOM.render(<Dashboard/>, document.getElementById('dashboard-main-container'));

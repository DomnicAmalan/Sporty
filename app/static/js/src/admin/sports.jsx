import React from 'react'
import ReactDOM from 'react-dom'
import axios from 'axios';
import { Pagination } from "../components/Pagination.jsx";




class Sports extends React.Component {

    constructor() {
        super();
        this.state = {
            exampleItems: [],
            pageOfItems: []
        };

        this.onChangePage = this.onChangePage.bind(this);
    }
    componentDidMount(){
        axios.get('/api/list/sports/all').then(res =>{
            this.setState({ exampleItems : res.data})
        })
    }

    onChangePage(pageOfItems) {
        this.setState({ pageOfItems: pageOfItems });
    }

    render() {
        return (
            <div>
                <div className="container">
                <div className="pagination-container">
                        <Pagination items={this.state.exampleItems} onChangePage={this.onChangePage} />
                    </div>
                    <div className="text-container">
                        {this.state.pageOfItems.map(item =>
                            <div className="list-grids" key={item._id}>{item.name}</div>
                        )}
                    </div>
                </div>
            </div>
        );
    }
}

ReactDOM.render(<Sports />, document.getElementById('sports-main-container'));
